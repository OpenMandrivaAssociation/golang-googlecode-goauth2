# Run tests in check section
%bcond_without check

%global goipath         golang.org/x/oauth2
%global forgeurl        https://github.com/golang/oauth2
%global commit          9dcd33a902f40452422c2367fefcb95b54f9f8f8

%global common_description %{expand:
A client implementation for OAuth 2.0 spec.}

%gometa

Name:           golang-googlecode-goauth2
Version:        0
Release:        0.28%{?dist}
Summary:        A client implementation for OAuth 2.0 spec
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(cloud.google.com/go/compute/metadata)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/net/context/ctxhttp)
BuildRequires: golang(google.golang.org/appengine)
BuildRequires: golang(google.golang.org/appengine/urlfetch)

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup

%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CONTRIBUTORS CONTRIBUTING.md AUTHORS


%changelog
* Fri Oct 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.28.20181026git9dcd33a
- Bump to upstream 9dcd33a902f40452422c2367fefcb95b54f9f8f8

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.27.git6881fee
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.26.git6881fee
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 09 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.25.git6881fee
- Drop the code.google.com/p/goauth2 variant of the import path prefix.
  It's no longer used. All projects that depends on it need to be updated
  or patched.

* Wed Mar 21 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.24.20180423git6881fee
- Bump to upstream 6881fee410a5daf86371371f9ad451b95e168b71
- Update to new Go packaging

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.23.git5432cc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.22.git5432cc9
- Bump to upstream 5432cc9688e6250a0dd8f5a5f4c781d92b398be6
  related: #1227273

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.21.git1364adb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.20.git1364adb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.19.git1364adb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.git1364adb
- Polish the spec file
  related: #1227273

* Mon Aug 01 2016 jchaloup <jchaloup@redhat.com> - 0-0.17.git1364adb
- Bump to upstream 1364adb2c63445016c5ed4518fc71f6a3cda6169
  related: #1227273

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.16.git8914e50
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.15.git8914e50
- Bump to upstream 8914e5017ca260f2a3a1575b1e6868874050d95e
  related: #1227273

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.14.gitb5adcc2
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitb5adcc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 20 2015 jchaloup <jchaloup@redhat.com> - 0-0.12.gitb5adcc2
- Choose the corret devel subpackage
  related: #1227273

* Wed Aug 19 2015 jchaloup <jchaloup@redhat.com> - 0-0.11.gitb5adcc2
- Update spec file to spec-2.0
  related: #1227273

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.hgb5adcc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 jchaloup <jchaloup@redhat.com> - 0-0.9.hgb5adcc2
- Update provides of golang-googlecode-goauth2.
  There were not missing, it is just different subpackage.
  related: #1227273

* Tue Jun 09 2015 jchaloup <jchaloup@redhat.com> - 0-0.8.hgb5adcc2
- Add missing Provides
  related: #1227273

* Tue Jun 02 2015 jchaloup <jchaloup@redhat.com> - 0-0.7.hgb5adcc2
- Bump to upstream b5adcc2dcdf009d0391547edc6ecbaff889f5bb9
  resolves: #1227273

* Sun Mar 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.hg267028f
- Add the latest commit of depricated code.google.com/o/goauth2 afe77d958c701557ec5dc56f6936fcc194d15520
  related: #1141822

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.hgafe77d958c70
- Bump to upstream 267028f9bc2a1177dc5769be38c68c1b4fbe91c4
  related: #1141822

* Tue Nov 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.4.hgafe77d958c70
- Choose the correct architecture
  related: #1141822

* Thu Sep 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.3.hgafe77d958c70
- Initial commit to git

* Mon Sep 15 2014 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0-0.2.hgafe77d958c70
- update to afe77d958c70
- preserve timestamps of copied files

* Mon Aug 04 2014 Adam Miller <maxamillion@fedoraproject.org> - 0-0.1.hg6a3615e294b5
- First package for Fedora.
